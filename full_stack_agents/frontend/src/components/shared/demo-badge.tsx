import { useAppStore } from '@/store/app-store'
import { Badge } from '@/components/ui/badge'

export function DemoBadge() {
  const { demoMode } = useAppStore()
  if (!demoMode) return null
  return (
    <Badge variant="outline" className="text-amber-400 border-amber-400/50">
      DEMO MODE
    </Badge>
  )
}
