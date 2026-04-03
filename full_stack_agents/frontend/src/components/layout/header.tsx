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
    <header className="flex items-center justify-between border-b border-border p-4">
      <h1 className="text-lg font-semibold">{title}</h1>
      <div className="flex items-center gap-3">
        <label className="text-sm text-muted-foreground">Demo Mode</label>
        <Switch checked={demoMode} onCheckedChange={toggleDemoMode} />
        {demoMode && (
          <Badge variant="outline" className="text-amber-400 border-amber-400/50">
            DEMO
          </Badge>
        )}
      </div>
    </header>
  )
}
