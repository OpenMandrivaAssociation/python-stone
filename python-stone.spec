Name:		python-stone
Version:	3.5.5
Release:	2
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
# setup.py declares no version: upstream derives it from git tags with
# setuptools-scm, so this BuildRequires is what makes it produce a real
# version at all. Without it setuptools falls back to 0.0.0, the dist-info
# directory becomes stone-0.0.0.dist-info, and the auto generator emits
# "Provides: python3.14dist(stone) = 0". That leaves every consumer that asks
# for a version range -- python-dropbox, and through it
# duplicity-backend-dropbox -- uninstallable.
BuildRequires:	python%{pyver}dist(setuptools_scm)
BuildSystem:	python
BuildArch:	noarch

%description
Stone is an interface description language (IDL) for APIs.

%prep
%autosetup -p1 -n stone-%{version}
touch requirements.txt

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%files
%{_bindir}/stone
%{py_sitedir}/stone
%{py_sitedir}/stone-*.*-info
