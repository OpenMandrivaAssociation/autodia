%define upstream_name	 Autodia

Name:		autodia
Version:	2.14
Release:	1

Summary:	Automatic Dia/UML generator
License:	GPL
Group:		Text tools
Url:		https://www.aarontrevena.co.uk/opensource/autodia/
Source0:	http://search.cpan.org/CPAN/authors/id/T/TE/TEEJAY/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
AutoDia is a modular application that parses source code or data (if a
handler is available) and produces an XML document in Dia format,
essentially a Dia diagram autocreation package. The diagrams its creates
are standard UML diagrams showing dependencies, superclasses, packages,
classes and inheritances, as well as the methods, etc of each class. 

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install
# what does script do there ?
rm -f %{buildroot}%{perl_vendorlib}/*.pl

%files
%doc CHANGES COPYING CREDITS FAQ README INSTALL TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*
