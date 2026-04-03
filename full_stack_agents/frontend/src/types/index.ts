export interface AgentInfo {
  role: string
  goal: string
  backstory: string
}

export interface BeginnerExample {
  id: string
  text: string
  label: string
}

export interface BeginnerRequest {
  text: string
  demo: boolean
}

export interface BeginnerResponse {
  verdict: 'hate_speech' | 'no_hate_speech'
  reasoning: string
  confidence: number
  agent_info: AgentInfo
}

export interface LogFile {
  name: string
  content: string
}

export interface IntermediateRequest {
  log_file: string
  demo: boolean
}

export interface PipelineStep {
  step: number
  agent_name: string
  status: 'idle' | 'running' | 'complete'
  output: string
}

export interface AdvancedRequest {
  stock: string
  demo: boolean
}

export interface AdvancedResult {
  company_info: Record<string, string>
  financial_analysis: string
  investment_recommendation: string
  recommendation_verdict: string
  timing: {
    parallel_time: number
    analysis_time: number
    total_time: number
    time_saved: number
  }
}

export type AppPage = 'home' | 'beginner' | 'intermediate' | 'advanced'
