Summary:	Provides throughput and sometimes progress on shell pipes.
Name:		pipemeter
Version:	0.8.3
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://spamaps.org/pipemeter.php
Source0:	http://spamaps.org/files/pipemeter/%{name}-%{version}.tar.gz
# Source0-md5:	3ecfb96bffbb3025124b72759026da2f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program can be used in a shell pipe to display speed and progress
(if size of stream is available).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 pipemeter $RPM_BUILD_ROOT%{_bindir}/pipemeter
install -D pipemeter.1 $RPM_BUILD_ROOT%{_mandir}/man1/pipemeter.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README results.txt testscript.sh
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
