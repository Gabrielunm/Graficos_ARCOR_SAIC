import os, re

chart_dir = r'C:\Users\gabri\Desktop\ARCOR\eecc\graficos'
files = ['01_rentabilidad.html','02_paradoja_inflacionaria.html','03_liquidez.html',
         '04_endeudamiento.html','05_desapalancamiento.html','06_actividad.html',
         '07_arcor_vs_indec.html','08_rotacion.html','10_capital_inmovilizacion.html',
         '11_flujo_efectivo.html','13_ocf_ratio.html']

for fname in files:
    path = os.path.join(chart_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract annotations with text between quotes
    # In plotly HTML, annotations are stored as JSON within the Plotly.newPlot call
    annotations = re.findall(r'"text":"((?:[^"\\]|\\.)*?)"', content)
    
    print(f'\n===== {fname} =====')
    for a in annotations:
        a_clean = a.replace('\\n', ' | ').replace('\\"', '"').replace('\\\\', '\\')
        keywords = ['ingredion', 'sayon', 'dubai', 'ON ', 'fixscr', 'moody', 
                    'la nacion', 'ambito', 'cronista', 'indec', 'recpam', 
                    'pandemia', 'jv', 'joint', 'dividend', 'convergen',
                    'crossover', 'ahogo', 'operaci', 'maximo', 'minimo',
                    'record', 'emision', 'refinanci', '350m', 'paradoja',
                    'inflacion', 'consumo', 'caida', 'brecha', 'export',
                    'EBITDA', 'ROE', 'ROA', 'Margen', 'Du', 'bica', 'Bica']
        if len(a) > 10 and any(kw.lower() in a_clean.lower() for kw in keywords):
            print(f'  ANN: {a_clean[:350]}')
