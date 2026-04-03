import { motion } from 'framer-motion'

interface MetricsGridProps {
  data: Record<string, string>
}

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.04 },
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
      className="grid grid-cols-2 gap-2.5 md:grid-cols-3 lg:grid-cols-4"
      variants={container}
      initial="hidden"
      animate="show"
    >
      {entries.map(([label, value]) => (
        <motion.div
          key={label}
          variants={item}
          className="rounded-lg border border-white/[0.06] bg-white/[0.02] p-3"
        >
          <p className="text-[10px] font-semibold uppercase tracking-wider text-primary/60">
            {label}
          </p>
          <p className="mt-1 text-sm font-bold">{value}</p>
        </motion.div>
      ))}
    </motion.div>
  )
}
