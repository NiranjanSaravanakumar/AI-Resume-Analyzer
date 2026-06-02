import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
  Tooltip,
} from 'recharts'

const LABELS = {
  technical_skills: 'Technical Skills',
  experience:       'Experience',
  projects:         'Projects',
  education:        'Education',
  achievements:     'Achievements',
  presentation:     'Presentation',
}

const CustomTooltip = ({ active, payload }) => {
  if (active && payload?.length) {
    const { subject, value } = payload[0].payload
    return (
      <div className="glass-card px-3 py-2 text-sm">
        <p className="text-slate-300 font-medium">{subject}</p>
        <p className="text-primary font-bold">{value} / 100</p>
      </div>
    )
  }
  return null
}

export default function ResumeRadarChart({ radarData }) {
  if (!radarData) return null

  const chartData = Object.entries(LABELS).map(([key, label]) => ({
    subject: label,
    value:   radarData[key] ?? 0,
    fullMark: 100,
  }))

  return (
    <div className="w-full h-80">
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={chartData} margin={{ top: 20, right: 50, bottom: 20, left: 50 }}>
          <PolarGrid stroke="rgba(123, 63, 242, 0.2)" strokeWidth={1} />
          <PolarAngleAxis
            dataKey="subject"
            tick={{ fill: '#e2e8f0', fontSize: 13, fontFamily: 'Inter', fontWeight: 600 }}
          />
          <PolarRadiusAxis
            angle={30}
            domain={[0, 100]}
            tick={{ fill: '#94a3b8', fontSize: 11, fontWeight: 500 }}
            tickCount={5}
            stroke="rgba(123, 63, 242, 0.15)"
          />
          <Radar
            name="Resume"
            dataKey="value"
            stroke="#7B3FF2"
            fill="#5D5CDE"
            fillOpacity={0.35}
            strokeWidth={2.5}
            dot={{ fill: '#43B8FF', r: 5, strokeWidth: 2, stroke: '#fff' }}
          />
          <Tooltip content={<CustomTooltip />} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  )
}
