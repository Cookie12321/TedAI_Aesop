import { useRouter } from "next/router";
import { Tooltip, Legend, XAxis, YAxis, CartesianGrid, ResponsiveContainer, LineChart, Line } from "recharts";
const DataPage = () => {
    const router = useRouter();
    const { data } = router.query as { data: string };
    console.log(data);
    const new_data = JSON.parse(data)
    return (
    <div>
        HI
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
                <YAxis />
                <Legend />
                <Tooltip />
                <Line type="monotone" dataKey="COM" stroke="#8884d8" />
                <Line type="monotone" dataKey="AFF" stroke="#8884d8" />
                <Line type="monotone" dataKey="EIR" stroke="#8884d8" />  
                <Line type="monotone" dataKey="EIM" stroke="#8884d8" />  
                <Line type="monotone" dataKey="SE" stroke="#8884d8" />
                <Line type="monotone" dataKey="SC" stroke="#8884d8" /> 
                <Line type="monotone" dataKey="AGG" stroke="#8884d8" /> 
                <Line type="monotone" dataKey="ICS" stroke="#8884d8" /> 
            </LineChart>
        </ResponsiveContainer>
    </div>
    )
  } 
  
  export default DataPage;