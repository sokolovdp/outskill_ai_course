import { useState } from 'react'
import { Shield } from 'lucide-react'
import { useAppStore } from '@/store/app-store'
import { useBeginnerExamples, useAnalyzeText } from '@/hooks/use-beginner'
import { DemoBadge } from '@/components/shared/demo-badge'
import { TextAnalyzer } from '@/components/beginner/text-analyzer'
import { ExampleChips } from '@/components/beginner/example-chips'
import { ResultVerdict } from '@/components/beginner/result-verdict'

export function BeginnerPage() {
  const { demoMode } = useAppStore()
  const { data: examples } = useBeginnerExamples()
  const { mutateAsync, data: result, isPending } = useAnalyzeText()
  const [inputText, setInputText] = useState('')

  const handleChipSelect = (text: string) => {
    setInputText(text)
    mutateAsync({ text, demo: demoMode })
  }

  const handleAnalyze = (text: string) => {
    mutateAsync({ text, demo: demoMode })
  }

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <div className="space-y-2">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 ring-1 ring-primary/20">
            <Shield className="h-5 w-5 text-primary" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-2xl font-bold">Content Shield</h2>
              <DemoBadge />
            </div>
            <p className="text-sm text-muted-foreground">
              Single-agent hate speech detection powered by CrewAI
            </p>
          </div>
        </div>
      </div>

      <TextAnalyzer
        onAnalyze={handleAnalyze}
        isLoading={isPending}
        value={inputText}
        onValueChange={setInputText}
      />

      {examples && examples.length > 0 && (
        <div className="space-y-3">
          <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
            Try an example
          </p>
          <ExampleChips examples={examples} onSelect={handleChipSelect} />
        </div>
      )}

      <ResultVerdict result={result ?? null} />
    </div>
  )
}
