import { useState } from 'react'
import { analyzeStockStream as analyzeStockStreamApi } from '@/lib/api'
import { useAppStore } from '@/store/app-store'
import { simulateAdvancedPipeline } from '@/lib/demo-data'
import type { AdvancedRequest } from '@/types'

export function useAnalyzeStock() {
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const demoMode = useAppStore((s) => s.demoMode)

  const analyzeStockStream = async (
    req: AdvancedRequest,
    onEvent: (data: Record<string, unknown>) => void,
  ) => {
    setIsAnalyzing(true)
    if (demoMode) {
      await simulateAdvancedPipeline(onEvent)
    } else {
      await analyzeStockStreamApi(req, onEvent)
    }
    setIsAnalyzing(false)
  }

  return { analyzeStockStream, isAnalyzing }
}
