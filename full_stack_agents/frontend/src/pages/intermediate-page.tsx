import { useState } from 'react'
import { Terminal, Loader2, ChevronDown } from 'lucide-react'
import { useAppStore } from '@/store/app-store'
import { useLogs, useAnalyzeLogs } from '@/hooks/use-intermediate'
import { Button } from '@/components/ui/button'
import { DemoBadge } from '@/components/shared/demo-badge'
import { LogViewer } from '@/components/intermediate/log-viewer'
import { PipelineFlow } from '@/components/intermediate/pipeline-flow'
import { ReportTabs } from '@/components/intermediate/report-tabs'
import type { PipelineStep } from '@/types'

const initialSteps: PipelineStep[] = [
  { step: 1, agent_name: 'Log Analyzer', status: 'idle', output: '' },
  { step: 2, agent_name: 'Issue Investigator', status: 'idle', output: '' },
  { step: 3, agent_name: 'Solution Specialist', status: 'idle', output: '' },
]

export function IntermediatePage() {
  const { demoMode } = useAppStore()
  const { data: logs } = useLogs()
  const { analyzeLogsStream, isAnalyzing } = useAnalyzeLogs()
  const [selectedLog, setSelectedLog] = useState('')
  const [steps, setSteps] = useState<PipelineStep[]>(initialSteps)

  const selectedLogContent =
    logs?.find((l) => l.name === selectedLog)?.content ?? ''

  const handleAnalyze = () => {
    if (!selectedLog) return
    setSteps(initialSteps)
    analyzeLogsStream({ log_file: selectedLog, demo: demoMode }, (step) => {
      setSteps((prev) =>
        prev.map((s) => (s.step === step.step ? step : s)),
      )
    })
  }

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 ring-1 ring-primary/20">
            <Terminal className="h-5 w-5 text-primary" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-2xl font-bold">DevOps Doctor</h2>
              <DemoBadge />
            </div>
            <p className="text-sm text-muted-foreground">
              Multi-agent pipeline for automated log analysis &mdash; parsing to diagnosis to remediation
            </p>
          </div>
        </div>
      </div>

      <div className="flex gap-3">
        <div className="relative flex-1">
          <select
            className="w-full appearance-none rounded-lg border border-white/[0.08] bg-white/[0.03] px-4 py-2.5 pr-10 text-sm text-foreground transition-colors hover:border-white/[0.12] focus:border-primary/50 focus:outline-none focus:ring-1 focus:ring-primary/30"
            value={selectedLog}
            onChange={(e) => setSelectedLog(e.target.value)}
          >
            <option value="" className="bg-card">
              Select a log file...
            </option>
            {logs?.map((log) => (
              <option key={log.name} value={log.name} className="bg-card">
                {log.name}
              </option>
            ))}
          </select>
          <ChevronDown className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
        </div>
        <Button
          onClick={handleAnalyze}
          disabled={!selectedLog || isAnalyzing}
          className="min-w-[160px]"
        >
          {isAnalyzing && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
          Start Analysis
        </Button>
      </div>

      <div className="grid gap-6 lg:grid-cols-5">
        <div className="lg:col-span-2 space-y-4">
          {selectedLogContent ? (
            <LogViewer content={selectedLogContent} />
          ) : (
            <div className="flex h-64 items-center justify-center rounded-lg border border-dashed border-white/[0.08] text-sm text-muted-foreground">
              Select a log file to preview
            </div>
          )}
        </div>

        <div className="lg:col-span-3 space-y-6">
          <PipelineFlow steps={steps} />
          <ReportTabs steps={steps} />
        </div>
      </div>
    </div>
  )
}
