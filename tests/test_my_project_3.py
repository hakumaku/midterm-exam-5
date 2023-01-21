import json

import pytest
import os

from pathlib import Path

RESOURCES = Path(os.path.dirname(__file__)).parent / "tests" / "resources"


@pytest.mark.parametrize("child", [f"child{i}" for i in range(1, 100, 2)])
@pytest.mark.parametrize("parent", [f"parent{i+1}" for i in range(10)])
def test_verify_all_odd_json_files_in_resource(parent, child):
    path = RESOURCES / parent / child
    for i in range(1, 101):
        with open(path / f"file{i}.json") as fp:
            data = json.load(fp)

        assert data["my_key1"] == "bar"
        assert data["my_key11"][0] == "bar"
        assert data["my_key12"]["#MyValue=1"] == "bar"


@pytest.mark.parametrize("child", [f"child{i}" for i in range(2, 101, 2)])
@pytest.mark.parametrize("parent", [f"parent{i+1}" for i in range(10)])
def test_verify_all_even_json_files_in_resource(parent, child):
    path = RESOURCES / parent / child
    for i in range(1, 101):
        with open(path / f"file{i}.json") as fp:
            data = json.load(fp)

        assert data["my_key1"] == "foo"
        assert data["my_key11"][0] == "foo"
        assert data["my_key12"]["#MyValue=1"] == "foo"


@pytest.mark.parametrize("child", [f"child{i}" for i in range(1, 100, 2)])
@pytest.mark.parametrize("parent", [f"parent{i+1}" for i in range(10)])
def test_verify_all_odd_txt_files_in_resource(parent, child):
    path = RESOURCES / parent / child
    for i in range(1, 101):
        with open(path / f"file{i}.txt") as fp:
            lines = fp.readlines()

        key, value = lines[92].split("=")
        assert key.strip() == "# MyValue"
        assert value.strip() == "100"


@pytest.mark.parametrize("child", [f"child{i}" for i in range(2, 101, 2)])
@pytest.mark.parametrize("parent", [f"parent{i+1}" for i in range(10)])
def test_verify_all_even_txt_files_in_resource(parent, child):
    path = RESOURCES / parent / child
    for i in range(1, 101):
        with open(path / f"file{i}.txt") as fp:
            lines = fp.readlines()

        key, value = lines[92].split("=")
        assert key.strip() == "MyValue"
        assert value.strip() == "1"
