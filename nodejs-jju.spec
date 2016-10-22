%{?scl:%scl_package nodejs-jju}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-jju

%global npm_name jju
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-jju
Version:	1.2.1
Release:	4%{?dist}
Summary:	a set of utilities to work with JSON / JSON5 documents
Url:		http://rlidwka.github.io/jju/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    LICENSE
License:	WTFPL
# http://www.wtfpl.net/txt/copying/

BuildArch:	noarch

ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(eslint)
BuildRequires:	%{?scl_prefix}npm(js-yaml)
BuildRequires:	%{?scl_prefix}npm(mocha)
%endif

%description
a set of utilities to work with JSON / JSON5 documents

%prep
%setup -q -n package
cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
mocha test/*.js
%endif

%files
%{nodejs_sitelib}/jju

%doc README.md LICENSE

%changelog
* Mon Jun 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.1-4
- Fix license

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.1-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.1-2
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.1-1
- Initial build
