import { motion } from 'framer-motion'
import { Database, Newspaper, BarChart3, Award, Check, ArrowDown } from 'lucide-react'
import { Card, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { cn } from '@/lib/utils'

interface Phase {
  name: string
  status: 'idle' | 'running' | 'complete'
  elapsed: number
}

interface ParallelLanesProps {
  phases: Phase[]
}

const phaseIcons: Record<string, React.ElementType> = {
  'Financial Data': Database,
  'News Research': Newspaper,
  'Analysis': BarChart3,
  'Recommendation': Award,
}

export function ParallelLanes({ phases }: ParallelLanesProps) {
  const parallelPhases = phases.filter((p) => ['Financial Data', 'News Research'].includes(p.name))
  const sequentialPhases = phases.filter((p) => ['Analysis', 'Recommendation'].includes(p.name))

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-4">
        {parallelPhases.map((phase) => {
          const Icon = phaseIcons[phase.name] ?? BarChart3
          return (
            <LaneCard key={phase.name} phase={phase} icon={Icon} />
          )
        })}
      </div>

      {sequentialPhases.length > 0 && (
        <div className="flex justify-center">
          <ArrowDown className="h-6 w-6 text-muted-foreground" />
        </div>
      )}

      <div className="grid grid-cols-2 gap-4">
        {sequentialPhases.map((phase) => {
          const Icon = phaseIcons[phase.name] ?? BarChart3
          return (
            <LaneCard key={phase.name} phase={phase} icon={Icon} />
          )
        })}
      </div>
    </div>
  )
}

function LaneCard({ phase, icon: Icon }: { phase: Phase; icon: React.ElementType }) {
  return (
    <Card>
      <CardContent className="p-4 space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Icon className="h-4 w-4 text-muted-foreground" />
            <span className="text-sm font-medium">{phase.name}</span>
          </div>
          <Badge
            variant="outline"
            className={cn(
              'text-xs',
              phase.status === 'idle' && 'text-muted-foreground border-muted',
              phase.status === 'running' && 'text-primary border-primary/50',
              phase.status === 'complete' && 'text-emerald-400 border-emerald-500/50',
            )}
          >
            {phase.status === 'complete' && <Check className="mr-1 h-3 w-3" />}
            {phase.status}
          </Badge>
        </div>

        {phase.status === 'running' && (
          <div className="h-1.5 w-full overflow-hidden rounded-full bg-muted">
            <motion.div
              className="h-full bg-primary rounded-full"
              animate={{ width: ['0%', '70%', '30%', '90%', '50%'] }}
              transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
            />
          </div>
        )}

        {phase.elapsed > 0 && (
          <p className="text-xs text-muted-foreground">
            {phase.elapsed.toFixed(1)}s
          </p>
        )}
      </CardContent>
    </Card>
  )
}
