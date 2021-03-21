import pygal

piechart = pygal.Pie()
piechart.reoder()

piechart = pygal.Pie()
piechart.tittle = "Favourite Pets"
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
piechart.render()

piechart = pygal.Bar()
piechart.tittle = "Programming Languages by number of Jobs on Indeed by Thousands"
piechart.add('Python', 19)
piechart.add('Java Script', 24)
piechart.add('Java', 29)
piechart.add('C#', 18)
piechart.add('C', 8)
piechart.add('C++', 9)
piechart.add('Go', 1.5)
piechart.add('Swift', 1.8)
piechart.add('PHP', 7)
piechart.render()