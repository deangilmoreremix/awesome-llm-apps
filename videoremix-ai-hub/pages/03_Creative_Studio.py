from shared.session_state import init_session_state
from shared.ui_components import render_css
from shared.page_builders import render_hub_page

init_session_state()
render_css()
render_hub_page("Creative Studio")