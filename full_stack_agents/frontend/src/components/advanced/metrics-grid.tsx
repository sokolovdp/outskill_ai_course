import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/card'

interface MetricsGridProps {
  data: Record<string, string>
}

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.05 },
  },
}

const item = {
  hidden: { opacity: 0, y: 10 },
  show: { opacity: 1, y: 0 },
}

export function MetricsGrid({ data }: MetricsGridProps) {
  const entries = Object.entries(data)

  return (
    <motion.div
      className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3"
      variants={container}
      initial="hidden"
      animate="show"
    >
      {entries.map(([label, value]) => (
        <motion.div key={label} variants={item}>
          <Card>
            <CardContent className="p-4">
              <p className="text-xs text-muted-foreground uppercase">{label}</p>
              <p className="text-lg font-semibold mt-1">{value}</p>
            </CardContent>
          </Card>
        </motion.div>
      ))}
    </motion.div>
  )
}
