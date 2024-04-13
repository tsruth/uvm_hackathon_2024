from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    num_routes = 6
    data = {
        'line': 'Redstone Express',
        'origin': 'Waterman',
        'destin': 'Redstone Green',
        'tt_O': 5,
        'tt_D': 10,
        'dist_O': '1.5',
        'sch_t_O': '1:30',
        'sch_t_D': '1:31'
    }
    
    routes=[]
    for i in range(num_routes):
        routes.append(data)

    return render_template('index.html', data=routes)

if __name__ == '__main__':
    app.run(debug=True)
