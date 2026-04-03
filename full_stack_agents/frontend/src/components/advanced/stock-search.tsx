import { useState } from 'react'
import { TrendingUp, Loader2 } from 'lucide-react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'

interface StockSearchProps {
  onSearch: (stock: string) => void
  isLoading: boolean
}

export function StockSearch({ onSearch, isLoading }: StockSearchProps) {
  const [stock, setStock] = useState('')

  const handleSearch = () => {
    if (stock.trim()) onSearch(stock.trim().toUpperCase())
  }

  return (
    <div className="flex gap-3">
      <Input
        placeholder="Enter stock symbol (e.g., RELIANCE)"
        value={stock}
        onChange={(e) => setStock(e.target.value.toUpperCase())}
        onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
        className="flex-1 border-white/[0.08] bg-white/[0.03] placeholder:text-muted-foreground/50"
      />
      <Button
        onClick={handleSearch}
        disabled={!stock.trim() || isLoading}
        className="min-w-[130px]"
      >
        {isLoading ? (
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
        ) : (
          <TrendingUp className="mr-2 h-4 w-4" />
        )}
        Analyze
      </Button>
    </div>
  )
}
