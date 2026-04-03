import { Link } from 'react-router-dom'
import { Shield, Terminal, TrendingUp } from 'lucide-react'
import { motion } from 'framer-motion'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

const projects = [
  {
    title: 'Content Shield',
    icon: Shield,
    badge: 'Beginner',
    badgeColor: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
    description: 'AI-powered hate speech detection using a single CrewAI agent with custom tools for content classification.',
    caseStudy: 'Case Study: Twitter/X',
    link: '/beginner',
  },
  {
    title: 'DevOps Doctor',
    icon: Terminal,
    badge: 'Intermediate',
    badgeColor: 'bg-amber-500/10 text-amber-400 border-amber-500/30',
    description: 'Multi-agent pipeline for automated log analysis, issue investigation, and solution recommendation.',
    caseStudy: 'Case Study: GitLab',
    link: '/intermediate',
  },
  {
    title: 'Market Intelligence',
    icon: TrendingUp,
    badge: 'Advanced',
    badgeColor: 'bg-red-500/10 text-red-400 border-red-500/30',
    description: 'Parallel multi-agent system for comprehensive financial analysis with real-time data aggregation.',
    caseStudy: 'Case Study: Morgan Stanley',
    link: '/advanced',
  },
]

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.15 },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export function HomePage() {
  return (
    <div className="relative">
      <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(6,182,212,0.08),transparent_70%)]" />

      <div className="relative space-y-12">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="space-y-4 text-center pt-12"
        >
          <h1 className="text-5xl font-bold bg-gradient-to-r from-primary to-cyan-300 bg-clip-text text-transparent">
            Agent Studio
          </h1>
          <p className="mx-auto max-w-2xl text-lg text-muted-foreground">
            Explore three AI agent patterns — from single-agent tools to parallel multi-agent orchestration — built with CrewAI and FastAPI.
          </p>
        </motion.div>

        <motion.div
          className="grid gap-6 md:grid-cols-3"
          variants={container}
          initial="hidden"
          animate="show"
        >
          {projects.map((project) => (
            <motion.div key={project.title} variants={item}>
              <Link to={project.link} className="block h-full">
                <Card className="h-full transition-all duration-200 hover:scale-[1.02] hover:border-primary/50">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <project.icon className="h-8 w-8 text-primary" />
                      <Badge
                        variant="outline"
                        className={project.badgeColor}
                      >
                        {project.badge}
                      </Badge>
                    </div>
                    <CardTitle className="mt-4">{project.title}</CardTitle>
                    <CardDescription>{project.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <p className="text-xs text-muted-foreground">{project.caseStudy}</p>
                    <Button variant="ghost" size="sm" className="mt-4 px-0 text-primary">
                      Explore →
                    </Button>
                  </CardContent>
                </Card>
              </Link>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  )
}
