import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs'
import { MarkdownRenderer } from '@/components/shared/markdown-renderer'
import type { PipelineStep } from '@/types'

interface ReportTabsProps {
  steps: PipelineStep[]
}

const tabLabels = ['Log Analysis', 'Investigation', 'Solution']

export function ReportTabs({ steps }: ReportTabsProps) {
  return (
    <Tabs defaultValue="0">
      <TabsList>
        {tabLabels.map((label, i) => (
          <TabsTrigger key={i} value={String(i)} disabled={steps[i]?.status === 'idle'}>
            {label}
          </TabsTrigger>
        ))}
      </TabsList>
      {tabLabels.map((_, i) => (
        <TabsContent key={i} value={String(i)}>
          {steps[i]?.output ? (
            <MarkdownRenderer content={steps[i].output} />
          ) : (
            <p className="py-8 text-center text-sm text-muted-foreground">
              Waiting for analysis...
            </p>
          )}
        </TabsContent>
      ))}
    </Tabs>
  )
}
