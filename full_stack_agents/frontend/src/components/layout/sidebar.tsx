import { NavLink } from 'react-router-dom'
import { Brain, Home, Shield, Terminal, TrendingUp } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
  { to: '/', label: 'Home', icon: Home },
  { to: '/beginner', label: 'Content Shield', icon: Shield },
  { to: '/intermediate', label: 'DevOps Doctor', icon: Terminal },
  { to: '/advanced', label: 'Market Intelligence', icon: TrendingUp },
]

export function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 flex h-screen w-64 flex-col border-r border-border bg-card">
      <div className="flex items-center gap-3 p-6">
        <Brain className="h-8 w-8 text-primary" />
        <span className="text-xl font-bold text-primary">Agent Studio</span>
      </div>
      <nav className="flex-1 space-y-1 px-3">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              cn(
                'flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-primary/10 text-primary'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground',
              )
            }
          >
            <item.icon className="h-5 w-5" />
            {item.label}
          </NavLink>
        ))}
      </nav>
      <div className="p-4">
        <p className="text-xs text-muted-foreground">Built with CrewAI</p>
      </div>
    </aside>
  )
}
