import { Sidebar } from '@/components/layout/sidebar'
import { Header } from '@/components/layout/header'

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-background text-foreground">
      <Sidebar />
      <div className="ml-60 flex flex-1 flex-col">
        <Header />
        <main className="relative flex-1 overflow-hidden">
          <div className="pointer-events-none absolute inset-0 dot-pattern" />
          <div className="relative p-6">{children}</div>
        </main>
      </div>
    </div>
  )
}
