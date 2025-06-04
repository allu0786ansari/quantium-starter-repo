import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app(dash_duo):
    # Import your app from app_task4.py
    app = import_app('app_task4')  # don't include .py
    dash_duo.start_server(app)
    return dash_duo


def test_header_is_present(dash_app):
    header = dash_app.find_element("h1")
    assert header.text == "Soul Foods Sales Visualizer"


def test_graph_is_present(dash_app):
    graph = dash_app.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_is_present(dash_app):
    radio = dash_app.find_element("#region-selector")
    assert radio is not None
