Summary:	Provides throughput and sometimes progress on shell pipes
Summary(pl):	Pokazywanie szybko¶ci przesy³ania i czasem postêpu dla potoków
Name:		pipemeter
Version:	0.9.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://spamaps.org/files/pipemeter/%{name}-%{version}.tar.gz
# Source0-md5:	d7cb23dce8c75fdfe85e609873b12d9c
URL:		http://spamaps.org/pipemeter.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program can be used in a shell pipe to display speed and progress
(if size of stream is available).

%description -l pl
Ten program mo¿e byæ u¿ywany w potoku do wy¶wietlania szybko¶ci i
postêpu przesy³ania danych (je¶li rozmiar strumienia jest znany).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D pipemeter $RPM_BUILD_ROOT%{_bindir}/pipemeter
install -D pipemeter.1 $RPM_BUILD_ROOT%{_mandir}/man1/pipemeter.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README results.txt testscript.sh
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
