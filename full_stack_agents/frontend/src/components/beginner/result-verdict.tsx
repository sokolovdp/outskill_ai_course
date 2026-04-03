import { motion } from 'framer-motion'
import { ShieldCheck, ShieldAlert } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'
import { AgentCard } from '@/components/shared/agent-card'
import type { BeginnerResponse } from '@/types'

interface ResultVerdictProps {
  result: BeginnerResponse | null
}

export function ResultVerdict({ result }: ResultVerdictProps) {
  if (!result) {
    return (
      <div className="flex items-center justify-center py-12 text-muted-foreground">
        Results will appear here
      </div>
    )
  }

  const isSafe = result.verdict === 'no_hate_speech'

  return (
    <motion.div
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ type: 'spring', duration: 0.5 }}
      className="space-y-4"
    >
      <div className="flex flex-col items-center gap-3 py-6">
        {isSafe ? (
          <ShieldCheck className="h-16 w-16 text-emerald-400" />
        ) : (
          <ShieldAlert className="h-16 w-16 text-red-400" />
        )}
        <span
          className={`text-2xl font-bold ${isSafe ? 'text-emerald-400' : 'text-red-400'}`}
        >
          {isSafe ? 'SAFE' : 'HATE SPEECH'}
        </span>
      </div>

      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm">
          <span className="text-muted-foreground">Confidence</span>
          <span className="font-medium">{Math.round(result.confidence * 100)}%</span>
        </div>
        <Progress value={result.confidence * 100} />
      </div>

      <Card>
        <CardHeader className="p-4 pb-2">
          <CardTitle className="text-sm">Reasoning</CardTitle>
        </CardHeader>
        <CardContent className="p-4 pt-0">
          <p className="text-sm text-muted-foreground">{result.reasoning}</p>
        </CardContent>
      </Card>

      {result.agent_info && <AgentCard agentInfo={result.agent_info} />}
    </motion.div>
  )
}
