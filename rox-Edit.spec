%include  /usr/lib/rpm/macros.python
%define _appsdir /usr/X11R6/share/ROX-apps
%define _name Edit
Summary:	ROX-Edit is a simple text editor
Summary(pl):	ROX-Edit jest prostym edytorem tekstu
Name:		rox-%{_name}
Version:	0.1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{_name}-%{version}.tgz
URL:		http://rox.sourceforge.net/rox_utils.php3
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-Edit is a very simple text editor written in Python.

%description -l pl
ROX-Edit hest bardzo prostym edytorem tekstu napisanym w Pythonie.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,icons}

install App* *.py Options.xml $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install icons/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/icons

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Options.xml
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/icons
%dir %{_appsdir}/%{_name}
