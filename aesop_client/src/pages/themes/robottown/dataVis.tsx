import { useRouter } from "next/router";
import { Tooltip, Legend, XAxis, YAxis, CartesianGrid, ResponsiveContainer, LineChart, Line } from "recharts";
const DataPage = () => {
    const router = useRouter();
    const { data } = router.query as { data: string };
    const { data_description } = router.query as { data_description: string }
    const SCORS_categories = ["COM","AFF", "EIR", "EIM", "SC", "AGG", "SE", "ICS"]
    const SEL_analysis = JSON.parse(data_description)
    const new_data = JSON.parse(data)
    return (
    <div>
        <h1>
            Sample Student 1
        </h1>
        <ResponsiveContainer width="100%" height={400} className="bg-gray-100">
            <LineChart
                width = {500}
                height = {300}
                data = {new_data}
                margin = {{
                    top: 5, right: 30, left: 20, bottom: 5
                }}

                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis tickCount={8}
                        tickSize={1}
                        allowDecimals={false}/>
                <Legend />
                <Tooltip />
                <Line type="monotone" dataKey="COM" stroke="#1F2937" />
                <Line type="monotone" dataKey="AFF" stroke="#847001" />
                <Line type="monotone" dataKey="EIR" stroke="#B341AE" />  
                <Line type="monotone" dataKey="EIM" stroke="#3B82F6" />  
                <Line type="monotone" dataKey="SE" stroke="#16A34A" />
                <Line type="monotone" dataKey="SC" stroke="#EF4444" /> 
                <Line type="monotone" dataKey="AGG" stroke="#10B981" /> 
                <Line type="monotone" dataKey="ICS" stroke="#F59E0B" /> 
            </LineChart>
        </ResponsiveContainer>
        <div>
        {SCORS_categories.map((category, index) => (
          <div>
            <h3>
              {category}
            </h3>
            <p>
              Score: {SEL_analysis[category].score}
            </p>
            <p>
              Description: {SEL_analysis[category].description}
            </p>
          </div>
        ))}
      </div>

    </div>
    )
  } 
  
  export default DataPage;