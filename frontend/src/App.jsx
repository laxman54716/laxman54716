
import React, {useEffect, useState} from 'react'
import axios from 'axios'

export default function App(){
  const [summary, setSummary] = useState({})
  const [products, setProducts] = useState([])
  useEffect(()=>{
    axios.get('/api/dashboard/summary').then(r=>setSummary(r.data)).catch(()=>{})
    axios.get('/api/products/').then(r=>setProducts(r.data)).catch(()=>{})
  },[])
  return (
    <div className="p-6 font-sans">
      <h1 className="text-2xl font-bold mb-4">Smart Inventory - Demo</h1>
      <div className="grid grid-cols-3 gap-4 mb-6">
        <div className="p-4 border rounded">{'Total Products: ' + (summary.total_products||0)}</div>
        <div className="p-4 border rounded">{'Total Suppliers: ' + (summary.total_suppliers||0)}</div>
        <div className="p-4 border rounded">{'Low Stock Items: ' + (summary.low_stock_count||0)}</div>
      </div>
      <h2 className="text-xl font-semibold mb-2">Products</h2>
      <table className="min-w-full border">
        <thead><tr><th className="border p-2">Name</th><th className="border p-2">Category</th><th className="border p-2">Qty</th></tr></thead>
        <tbody>
          {products.map(p=>(
            <tr key={p.id}><td className="border p-2">{p.name}</td><td className="border p-2">{p.category}</td><td className="border p-2">{p.quantity}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
