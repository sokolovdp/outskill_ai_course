import { useState } from 'react'
import { Loader2 } from 'lucide-react'
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

  const selectedLogContent = logs?.find((l) => l.name === selectedLog)?.content ?? ''

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
    <div className="space-y-6">
      <div className="flex items-center gap-3">
        <h2 className="text-2xl font-bold">DevOps Doctor</h2>
        <DemoBadge />
      </div>
      <p className="text-muted-foreground">
        Multi-agent pipeline for automated log analysis — from parsing to diagnosis to remediation.
      </p>

      <div className="grid gap-6 lg:grid-cols-5">
        <div className="lg:col-span-2 space-y-4">
          <select
            className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
            value={selectedLog}
            onChange={(e) => setSelectedLog(e.target.value)}
          >
            <option value="">Select a log file...</option>
            {logs?.map((log) => (
              <option key={log.name} value={log.name}>
                {log.name}
              </option>
            ))}
          </select>

          {selectedLogContent && <LogViewer content={selectedLogContent} />}
        </div>

        <div className="lg:col-span-3 space-y-6">
          <Button
            onClick={handleAnalyze}
            disabled={!selectedLog || isAnalyzing}
            className="w-full"
          >
            {isAnalyzing ? (
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            ) : null}
            Start Analysis
          </Button>

          <PipelineFlow steps={steps} />
          <ReportTabs steps={steps} />
        </div>
      </div>
    </div>
  )
}
