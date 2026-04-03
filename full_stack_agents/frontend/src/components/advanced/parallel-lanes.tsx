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
  Analysis: BarChart3,
  Recommendation: Award,
}

export function ParallelLanes({ phases }: ParallelLanesProps) {
  const parallelPhases = phases.filter((p) =>
    ['Financial Data', 'News Research'].includes(p.name),
  )
  const sequentialPhases = phases.filter((p) =>
    ['Analysis', 'Recommendation'].includes(p.name),
  )

  return (
    <div className="space-y-3">
      <div className="grid grid-cols-2 gap-3">
        {parallelPhases.map((phase) => (
          <LaneCard
            key={phase.name}
            phase={phase}
            icon={phaseIcons[phase.name] ?? BarChart3}
          />
        ))}
      </div>

      <div className="flex justify-center">
        <ArrowDown className="h-5 w-5 text-muted-foreground/50" />
      </div>

      <div className="grid grid-cols-2 gap-3">
        {sequentialPhases.map((phase) => (
          <LaneCard
            key={phase.name}
            phase={phase}
            icon={phaseIcons[phase.name] ?? BarChart3}
          />
        ))}
      </div>
    </div>
  )
}

function LaneCard({
  phase,
  icon: Icon,
}: {
  phase: Phase
  icon: React.ElementType
}) {
  return (
    <Card
      className={cn(
        'transition-all duration-300',
        phase.status === 'running' && 'border-primary/30 glow-sm',
        phase.status === 'complete' && 'border-emerald-500/20',
      )}
    >
      <CardContent className="space-y-3 p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div
              className={cn(
                'flex h-7 w-7 items-center justify-center rounded-md',
                phase.status === 'idle' && 'bg-muted',
                phase.status === 'running' && 'bg-primary/10',
                phase.status === 'complete' && 'bg-emerald-500/10',
              )}
            >
              <Icon
                className={cn(
                  'h-3.5 w-3.5',
                  phase.status === 'idle' && 'text-muted-foreground',
                  phase.status === 'running' && 'text-primary',
                  phase.status === 'complete' && 'text-emerald-400',
                )}
              />
            </div>
            <span className="text-sm font-medium">{phase.name}</span>
          </div>
          <Badge
            variant="outline"
            className={cn(
              'text-[10px] font-semibold tracking-wider',
              phase.status === 'idle' &&
                'border-white/[0.06] text-muted-foreground',
              phase.status === 'running' &&
                'border-primary/30 text-primary',
              phase.status === 'complete' &&
                'border-emerald-500/30 text-emerald-400',
            )}
          >
            {phase.status === 'complete' && (
              <Check className="mr-1 h-3 w-3" />
            )}
            {phase.status}
          </Badge>
        </div>

        {phase.status === 'running' && (
          <div className="h-1 w-full overflow-hidden rounded-full bg-muted">
            <motion.div
              className="h-full rounded-full bg-primary"
              animate={{ width: ['0%', '70%', '30%', '90%', '50%'] }}
              transition={{
                duration: 2,
                repeat: Infinity,
                ease: 'easeInOut',
              }}
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
