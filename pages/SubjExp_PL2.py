import streamlit as st
import pyvista as pv
#from stpyvista import stpyvista
from stpyvista.trame_backend import stpyvista
import mimetypes
import numpy as np
import random
import sys, os
from datetime import datetime, date
#import matplotlib.pyplot as plt
#import streamlit.components.v1 as components
#from streamlit.web.server.server import Server
#from streamlit_js_eval import streamlit_js_eval

###  Pyvista colors : 
###	   https://docs.pyvista.org/api/utilities/_autosummary/pyvista.color.name
### 
###  stpyvista :
###    https://stpyvista.streamlit.app/
### 
###  https://github.com/pyvista/pyvista-support/issues/59
###  https://github.com/pyvista/pyvista/issues/1790#issuecomment-981148635
###
### Mise en cache:
###  https://blog.streamlit.io/common-app-problems-resource-limits/
###  https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data
###  https://docs.streamlit.io/develop/concepts/architecture/caching
###  
###  https://discuss.streamlit.io/t/visualization-of-stl-files/27050/2
###
###  https://discuss.streamlit.io/t/input-widgets-inside-a-while-loop/34696/4    ????
###
  

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


cnt = st.session_state.count
#st.write(cnt)


#@st.cache_data
#@st.cache_resource
def read_and_display_stl(plname):
	plotter = pv.Plotter(window_size=[320,320])

	mesh = pv.read(plname)
	mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]

	## Add mesh to the plotter
	plotter.add_mesh(mesh, scalars='myscalar')
	#del mesh

	plotter.view_isometric()
	plotter.background_color = 'gainsboro'

	return(plotter)


# Create side-by-side columns
col10, col20, col30, col40, col50 = st.columns(5)


if cnt < st.session_state.nb_im:
	with col30:

		plotter0 = read_and_display_stl(st.session_state.pl2[cnt*6+1])

		## Send to streamlit
		stpyvista(plotter0, key=str(cnt))

	# Create side-by-side columns
	col1, col2, col3, col4, col5 = st.columns(5)


	with col1:

		plotter1 = read_and_display_stl(st.session_state.pl2[cnt*6+1+1])

		## Send to streamlit
		stpyvista(plotter1, key=str(cnt+1))

		option1 = st.selectbox('Bifurcation # 1',
		['Choose a score',1,2,3,4,5], index = None, key='selection1')
		#st.write('Score:', option1)
		#st.write(st.session_state.PL[cnt*6+1+1])
		st.session_state.Score1=option1


	with col2:

		plotter2 = read_and_display_stl(st.session_state.pl2[cnt*6+1+2])

		## Send to streamlit
		stpyvista(plotter2, key=str(cnt+2))

		option2 = st.selectbox('Bifurcation # 2',
		['Choose a score',1,2,3,4,5], index = None, key='selection2')
		#st.write('Score:', option2)
		#st.write(st.session_state.PL[cnt*6+1+2])
		st.session_state.Score2=option2


	with col3:

		plotter3 = read_and_display_stl(st.session_state.pl2[cnt*6+1+3])

		## Send to streamlit
		stpyvista(plotter3, key=str(cnt+3))

		option3 = st.selectbox('Bifurcation # 3',
		['Choose a score',1,2,3,4,5], index = None, key='selection3')
		#st.write('Score:', option3)
		#st.write(st.session_state.PL[cnt*6+1+3])
		st.session_state.Score3=option3


	with col4:

		plotter4 = read_and_display_stl(st.session_state.pl2[cnt*6+1+4])

		## Send to streamlit
		stpyvista(plotter4, key=str(cnt+4))

		option4 = st.selectbox('Bifurcation # 4',
		['Choose a score',1,2,3,4,5], index = None, key='selection4')
		#st.write('Score:', option4)
		#st.write(st.session_state.PL[cnt*6+1+4])
		st.session_state.Score4=option4


	with col5:

		plotter5 = read_and_display_stl(st.session_state.pl2[cnt*6+1+5])

		## Send to streamlit
		stpyvista(plotter5, key=str(cnt+5))

		option5 = st.selectbox('Bifurcation # 5',
		['Choose a score',1,2,3,4,5], index = None, key='selection5')
		#st.write('Score:', option5)
		#st.write(st.session_state.PL[cnt*6+1+5])
		st.session_state.Score5=option5


#components.html("""<hr style="height:6px;border:none;color:#222;background-color:#222;" /> """)
st.markdown("""---""")


if cnt == st.session_state.nb_im:
	st.session_state.count = 0
	st.session_state.PL = []
	del st.session_state["count"]
	del st.session_state["pl2"]
	st.switch_page("pages/end.py")



if cnt == st.session_state.nb_im - 1:
	endtime = datetime.now()
	with open("./outputs/" + st.session_state.time0 + ".txt", "a") as myfile:
		myfile.write("\nTest duration : %.3f min\n" %((endtime-st.session_state.t0).total_seconds()/60)), 



def update_counter():
	st.session_state.count += 1

	if (st.session_state.count >= 1):
		with open("./outputs/" + st.session_state.time0 + "_PL2.txt", "a") as myfile:
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+1]), '0'))
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+2]), st.session_state.Score1))
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+3]), st.session_state.Score2))
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+4]), st.session_state.Score3))
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+5]), st.session_state.Score4))
			myfile.write("%s,%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+6]), st.session_state.Score5))

			#myfile.write("%s\n%s\t%s\t%s\t%s\t%s\n" %(os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+1]), 
			#										os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+1+1]), 
			#										os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+2+1]), 
			#										os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+3+1]), 
			#										os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+4+1]), 
			#										os.path.basename(st.session_state.pl2[(st.session_state.count-1)*6+5+1])))
			#myfile.write("%s\t%s\t%s\t%s\t%s\n" %(st.session_state.Score1, 
			#									  st.session_state.Score2, 
			#									  st.session_state.Score3, 
			#									  st.session_state.Score4, 
			#									  st.session_state.Score5))
 

def reset_selectboxes():
	st.session_state.selection1 = 'Choose a score'
	st.session_state.selection2 = 'Choose a score'
	st.session_state.selection3 = 'Choose a score'
	st.session_state.selection4 = 'Choose a score'
	st.session_state.selection5 = 'Choose a score'


def master_callback():
	update_counter()
	#st.cache_data.clear()
	#st.cache_resource.clear()
	#st.cache_data.clear()
	#read_and_display_stl.clear()
	reset_selectboxes()


runButton = st.button("Validate", on_click=master_callback)

