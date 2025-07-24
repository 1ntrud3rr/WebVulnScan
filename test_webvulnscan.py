import pytest
from modules import port_scan, dir_brute, cms_detect, headers_check, subdomains, vuln_scan

def test_port_scan():
    output = port_scan.scan("example.com")
    assert isinstance(output, str)

def test_dir_brute():
    output = dir_brute.scan("example.com", delay=0, wordlist_path=None, threads=5)
    assert isinstance(output, str)

def test_cms_detect():
    output = cms_detect.scan("example.com")
    assert isinstance(output, str)

def test_headers_check():
    output = headers_check.scan("example.com")
    assert isinstance(output, str)

def test_subdomains():
    output = subdomains.scan("example.com")
    assert isinstance(output, str)

def test_vuln_scan():
    output = vuln_scan.scan("example.com")
    assert isinstance(output, str)
