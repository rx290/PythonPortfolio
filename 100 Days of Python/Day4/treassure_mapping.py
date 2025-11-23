

m_l = [['⬜️','⬜️','⬜️'],['⬜️','⬜️','⬜️'],['⬜️','⬜️','⬜️']]

def map(map_layout):
    column = map_layout[0]
    row = map_layout[1]
    for i in range(len(m_l)):
        if i == int(row)-1:
            m_l[i][int(column)-1]= 'x'
    
    print('',m_l[0],"\n",m_l[1],"\n",m_l[2])


map_layout = input("Please Enter Map layout")
map(map_layout)
