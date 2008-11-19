Summary:	A command line utility to convert HTML document to plain text
Summary(pl.UTF-8):	Narzędzie działające z linii poleceń do konwersji dokumentów HTML do czystego tekstu
Name:		html2text
Version:	1.3.2a
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://userpage.fu-berlin.de/%7Embayer/tools/%{name}-%{version}.tar.gz
# Source0-md5:	6097fe07b948e142315749e6620c9cfc
URL:		http://userpage.fu-berlin.de/~mbayer/tools/html2text.html
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
html2text is a command line utility, written in C++, that converts
HTML documents into plain text.

%description -l pl.UTF-8
html2text jest programem działającym z linii poleceń do konwersji
dokumentów HTML do czystego tekstu.

%prep
%setup -q

%build
%configure
%{__make} \
	CXX="%{__cxx}" \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
gzip -d *.gz
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -D %{name}rc.5 $RPM_BUILD_ROOT%{_mandir}/man5/%{name}rc.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS KNOWN_BUGS RELEASE_NOTES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
