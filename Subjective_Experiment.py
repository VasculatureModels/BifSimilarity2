import streamlit as st
from datetime import datetime, date
#from screeninfo import get_monitors
#import time
import numpy as np
import random

now = datetime.now()
start_time = now.strftime("%H:%M:%S")

st.set_page_config(initial_sidebar_state="collapsed" )

if 'time0' not in st.session_state:
	st.session_state.time0 = start_time

if 't0' not in st.session_state:
	st.session_state.t0 = datetime.now()

if 'st' not in st.session_state:
	st.session_state.st = False
if 'n' not in st.session_state:
	st.session_state.n = 0

if 'count' not in st.session_state:
	st.session_state.count = 0

if 'Score1' not in st.session_state:
	st.session_state.Score1 = 0
if 'Score2' not in st.session_state:
	st.session_state.Score2 = 0
if 'Score3' not in st.session_state:
	st.session_state.Score3 = 0
if 'Score4' not in st.session_state:
	st.session_state.Score4 = 0
if 'Score5' not in st.session_state:
	st.session_state.Score5 = 0


if 'pl1' not in st.session_state:

	st.session_state.pl1 = []

	playlist1 = np.genfromtxt("playlist_1.txt",usecols=(0),dtype=None, encoding=None)
	nb_im = int(playlist1[0])

	if 'nb_im' not in st.session_state:
		nb_im = int(playlist1[0])
		st.session_state.nb_im = nb_im

	index = np.arange(nb_im-1)

	idx=0
	if st.session_state.count == 0 and idx == 0: 
		random.shuffle(index)
		idx = idx + 1
	#print(index)

	st.session_state.pl1.append(playlist1[0])

	index = np.append(index,nb_im-1)

	scrambleIdx = np.array([2,3,4,5,6])
	random.shuffle(scrambleIdx)

	for i in range(len(index)):
		st.session_state.pl1.append(playlist1[index[i]*6+1])
		st.session_state.pl1.append(playlist1[index[i]*6+scrambleIdx[0]])
		st.session_state.pl1.append(playlist1[index[i]*6+scrambleIdx[1]])
		st.session_state.pl1.append(playlist1[index[i]*6+scrambleIdx[2]])
		st.session_state.pl1.append(playlist1[index[i]*6+scrambleIdx[3]])
		st.session_state.pl1.append(playlist1[index[i]*6+scrambleIdx[4]])


if 'pl2' not in st.session_state:

	st.session_state.pl2 = []

	playlist2 = np.genfromtxt("playlist_2.txt",usecols=(0),dtype=None, encoding=None)
	nb_im = int(playlist2[0])

	if 'nb_im' not in st.session_state:
		nb_im = int(playlist2[0])
		st.session_state.nb_im = nb_im

	index = np.arange(nb_im-1)

	idx=0
	if st.session_state.count == 0 and idx == 0: 
		random.shuffle(index)
		idx = idx + 1
	#print(index)

	st.session_state.pl2.append(playlist2[0])

	index = np.append(index,nb_im-1)

	scrambleIdx = np.array([2,3,4,5,6])
	random.shuffle(scrambleIdx)

	for i in range(len(index)):
		st.session_state.pl2.append(playlist2[index[i]*6+1])
		st.session_state.pl2.append(playlist2[index[i]*6+scrambleIdx[0]])
		st.session_state.pl2.append(playlist2[index[i]*6+scrambleIdx[1]])
		st.session_state.pl2.append(playlist2[index[i]*6+scrambleIdx[2]])
		st.session_state.pl2.append(playlist2[index[i]*6+scrambleIdx[3]])
		st.session_state.pl2.append(playlist2[index[i]*6+scrambleIdx[4]])



st.markdown(
	"""

	## &nbsp;&nbsp;The goal of this subjective experiment is to assess the similarities between cerebral bifurcations.

	&nbsp;&nbsp;A reference bifurcation will be displayed on the upper part of the screen, and 5 different test versions will be displayed underneath.

	&nbsp;&nbsp;Above each test version, a dropdown menu is used to sort the bifurcation with decreasing similarity.

	&nbsp;&nbsp;i.e. a score of "1" means "strong similarity with the refrerence", whereas a score of "5" means "both bifurcations strongly differ".

	## &nbsp;&nbsp;Protocol description:

	&nbsp;&nbsp;The observers shall use the 5 dropdown menus to score the similarities, and then validate using the button located at the bottom of the page.
	"""
#	&nbsp;&nbsp;
#	"""
)

st.write("There are %d successive displays being presented to the observers, the test duration is about 20 to 25 minutes." %(st.session_state.nb_im-1))

st.markdown(
	"""

	## &nbsp;&nbsp;Controls :
	+ For each 3D display, the user can rotate the bifurcation using the left mouse button.
	+ It is also possible to zoom (in/out), using the scroll wheel.
	+ The display can also be shifted (by holding the 'SHIFT' key, while dragging the image).

	"""
)

st.markdown("""---""")

if st.button("Launch Experiment #1"):
	st.switch_page("pages/SubjExp_PL1.py")

st.markdown("""---""")

if st.button("Launch Experiment #2"):
	st.switch_page("pages/SubjExp_PL2.py")
	

	#st.session_state.st = not st.session_state.st
	#st.session_state.n = 0
	#st.switch_page("pages/SubjExp_5_disp_B.py")
