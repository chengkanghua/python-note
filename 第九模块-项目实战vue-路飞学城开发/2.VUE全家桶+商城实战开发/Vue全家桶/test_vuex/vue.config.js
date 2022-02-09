const products = [
    { id: 1, title: 'iphone11', price: 800, inventory: 10 },
    { id: 2, title: 'iphone11 pro', price: 1200, inventory: 15 },
    { id: 3, title: 'iphone11 max', price: 1500, inventory: 5 },
]
module.exports = {
    devServer: {
        before(app, serve) {
            app.get('/api/products', (req, res) => {
                res.json({
                    results: products
                })
            })
        }
    }
}