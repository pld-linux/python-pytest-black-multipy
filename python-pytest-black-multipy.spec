#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (no tests in sources)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Allow '--black' on older Pythons
Summary(pl.UTF-8):	Dopuszczenie '--black' na starszych wersjach Pythona
Name:		python-pytest-black-multipy
Version:	1.0.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-black-multipy/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-black-multipy/pytest-black-multipy-%{version}.tar.gz
# Source0-md5:	4b6bf432b618c26178da323a782ee620
URL:		https://pypi.org/project/pytest-black-multipy/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:31.0.1
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-pytest >= 3.5
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:31.0.1
%if %{with tests}
BuildRequires:	python3-pytest >= 3.5
%if "%{py3_ver}" >= "3.6"
BuildRequires:	python3-pytest-black
%endif
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wrapper around pytest-black to allow projects on older Python
versions to use the --black parameter.

This project is deprecated. Instead, use pytest-enabler to enable
black when present.

%description -l pl.UTF-8
Obudowanie wokół pytest-black, pozwalające na korzystanie z parametru
"--black" w projektach budowanych na starszych wersjach Pythona.

Ten projekt jest przestarzały. Lepiej używać modułu pytest-enabler,
abyt włączyć black, kiedy jest dostępny.

%package -n python3-pytest-black-multipy
Summary:	Allow '--black' on older Pythons
Summary(pl.UTF-8):	Dopuszczenie '--black' na starszych wersjach Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pytest-black-multipy
A wrapper around pytest-black to allow projects on older Python
versions to use the --black parameter.

This project is deprecated. Instead, use pytest-enabler to enable
black when present.

%description -n python3-pytest-black-multipy -l pl.UTF-8
Obudowanie wokół pytest-black, pozwalające na korzystanie z parametru
"--black" w projektach budowanych na starszych wersjach Pythona.

Ten projekt jest przestarzały. Lepiej używać modułu pytest-enabler,
abyt włączyć black, kiedy jest dostępny.

%package apidocs
Summary:	API documentation for Python pytest-black-multipy module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pytest-black-multipy
Group:		Documentation

%description apidocs
API documentation for Python pytest-black-multipy module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pytest-black-multipy.

%prep
%setup -q -n pytest-black-multipy-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest ...
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest ...
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_black_multipy
%{py_sitescriptdir}/pytest_black_multipy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-black-multipy
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_black_multipy
%{py3_sitescriptdir}/pytest_black_multipy-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
