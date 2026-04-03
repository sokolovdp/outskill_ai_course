import { motion } from 'framer-motion'
import { Check } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { cn } from '@/lib/utils'

interface PipelineNodeProps {
  stepNumber: number
  name: string
  status: 'idle' | 'running' | 'complete'
  icon: React.ElementType
  description?: string
}

export function PipelineNode({ stepNumber, name, status, icon: Icon, description }: PipelineNodeProps) {
  return (
    <div className="flex items-center gap-4">
      <div
        className={cn(
          'flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-sm font-bold transition-colors',
          status === 'idle' && 'bg-muted text-muted-foreground',
          status === 'running' && 'bg-primary/20 text-primary',
          status === 'complete' && 'bg-emerald-500/20 text-emerald-400',
        )}
      >
        {status === 'complete' ? (
          <Check className="h-5 w-5" />
        ) : status === 'running' ? (
          <motion.div
            animate={{ scale: [1, 1.2, 1] }}
            transition={{ duration: 1.5, repeat: Infinity }}
            className="flex items-center justify-center"
          >
            <Icon className="h-5 w-5" />
          </motion.div>
        ) : (
          <span>{stepNumber}</span>
        )}
      </div>
      <div className="flex-1">
        <div className="flex items-center gap-2">
          <span className="text-sm font-medium">{name}</span>
          <Badge
            variant="outline"
            className={cn(
              'text-xs',
              status === 'idle' && 'text-muted-foreground border-muted',
              status === 'running' && 'text-primary border-primary/50',
              status === 'complete' && 'text-emerald-400 border-emerald-500/50',
            )}
          >
            {status}
          </Badge>
        </div>
        {description && <p className="text-xs text-muted-foreground">{description}</p>}
      </div>
    </div>
  )
}
