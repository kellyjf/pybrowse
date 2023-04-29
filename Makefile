
ui_%.py : %.ui
	pyuic5 -i 0 -o $@ $<

ui : ui_browser.py

test: ui
	./app_browser.py

