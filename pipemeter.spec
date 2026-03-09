Summary:	Provides throughput and sometimes progress on shell pipes
Summary(pl.UTF-8):	Pokazywanie szybkości przesyłania i czasem postępu dla potoków
Name:		pipemeter
Version:	1.1.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	https://launchpad.net/pipemeter/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	3900d8a848eaed2e9f5bfd6af0491173
URL:		https://launchpad.net/pipemeter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program can be used in a shell pipe to display speed and progress
(if size of stream is available).

%description -l pl.UTF-8
Ten program może być używany w potoku do wyświetlania szybkości i
postępu przesyłania danych (jeśli rozmiar strumienia jest znany).

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
