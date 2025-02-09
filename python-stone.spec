Name:		python-stone
Version:	3.3.8
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/stone/stone-%{version}.tar.gz
Summary:	Stone is an interface description language (IDL) for APIs.
URL:		https://pypi.org/project/stone/
License:	MIT License
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-runner)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
Stone is an interface description language (IDL) for APIs.

%prep
%autosetup -p1 -n stone-%{version}
sed -i -e 's,pytest-runner ==,pytest-runner >=,g' setup.py
ln -s test/requirements.txt .

%files
%{_bindir}/stone
%{py_sitedir}/stone
%{py_sitedir}/stone-*.*-info
