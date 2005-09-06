%define _name Edit
Summary:	ROX-Edit is a simple text editor
Summary(pl):	ROX-Edit jest prostym edytorem tekstu
Name:		rox-%{_name}
Version:	1.9.7
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/edit-%{version}.tgz
# Source0-md5:	a53920438d021640dbd4f573aa35bd76
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/Edit
Requires:	python-pygtk-gtk
Requires:	rox >= 2.3
Requires:	rox-Lib2
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Edit is a very simple text editor written in Python.

%description -l pl
ROX-Edit jest bardzo prostym edytorem tekstu napisanym w Pythonie.

%prep
%setup -q -n edit-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,Messages,images}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd %{_name}
install .DirIcon App* *.py Options.xml $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages
install images/* $RPM_BUILD_ROOT%{_roxdir}/%{_name}/images
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{_name}/Help/{Changes,README}
%defattr(644,root,root,755)
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/*.py[co]
%{_roxdir}/%{_name}/Help
%dir %{_roxdir}/%{_name}/Messages
%lang(de) %{_roxdir}/%{_name}/Messages/de.gmo
%lang(es) %{_roxdir}/%{_name}/Messages/es.gmo
%lang(fr) %{_roxdir}/%{_name}/Messages/fr.gmo
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%lang(zh_CN) %{_roxdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_roxdir}/%{_name}/Messages/zh_TW.gmo
%dir %{_roxdir}/%{_name}/images
%{_roxdir}/%{_name}/images/*.png
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
