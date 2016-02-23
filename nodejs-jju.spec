%{?scl:%scl_package nodejs-jju}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-jju

%global npm_name jju
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-jju
Version:	1.2.1
Release:	3%{?dist}
Summary:	a set of utilities to work with JSON / JSON5 documents
Url:		http://rlidwka.github.io/jju/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	{"type"=>"WTFPL", "url"=>"http://www.wtfpl.net/txt/copying/"}

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(eslint)
BuildRequires:	%{?scl_prefix}npm(js-yaml)
BuildRequires:	%{?scl_prefix}npm(mocha)
%endif

%description
a set of utilities to work with JSON / JSON5 documents

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/jju

%doc README.md

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.1-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.1-2
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.1-1
- Initial build
