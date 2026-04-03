import { useLocation } from 'react-router-dom'
import { useAppStore } from '@/store/app-store'
import { Switch } from '@/components/ui/switch'
import { Badge } from '@/components/ui/badge'

const pageTitles: Record<string, string> = {
  '/': 'Home',
  '/beginner': 'Content Shield',
  '/intermediate': 'DevOps Doctor',
  '/advanced': 'Market Intelligence',
}

export function Header() {
  const { pathname } = useLocation()
  const { demoMode, toggleDemoMode } = useAppStore()
  const title = pageTitles[pathname] ?? 'Agent Studio'

  return (
    <header className="sticky top-0 z-10 glass border-b border-white/[0.06] px-6 py-3">
      <div className="flex items-center justify-between">
        <h1 className="text-sm font-semibold tracking-wide text-foreground/70 uppercase">
          {title}
        </h1>
        <div className="flex items-center gap-3">
          <span className="text-xs text-muted-foreground">Demo Mode</span>
          <Switch checked={demoMode} onCheckedChange={toggleDemoMode} />
          {demoMode && (
            <Badge
              variant="outline"
              className="bg-amber-500/10 text-amber-400 border-amber-500/20 text-[10px] font-semibold tracking-wider"
            >
              DEMO
            </Badge>
          )}
        </div>
      </div>
    </header>
  )
}
