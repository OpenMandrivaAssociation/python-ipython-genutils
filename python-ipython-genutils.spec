%define srcname ipython_genutils

Name:		python-ipython-genutils
Summary:	Vestigial utilities from IPython
Version:	0.2.0
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://ipython.org/
Source0:	https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildSystem: python

%description
Pretend this doesn’t exist. Nobody should use it.
Only there as a dependency for ipython.

%files
%{python_sitelib}/ipython_genutils-%{version}-py*.*.egg-info
%{python_sitelib}/ipython_genutils/
