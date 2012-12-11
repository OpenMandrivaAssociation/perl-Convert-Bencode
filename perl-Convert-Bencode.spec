%define upstream_name    Convert-Bencode
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Functions for converting to/from bencoded strings
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Convert-Bencode/
Source0:	http://www.cpan.org/authors/id/O/OR/ORCLEV/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.45

BuildArch:	noarch

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*



%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 657399
- rebuild for updated spec-helper

* Wed Mar 09 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.30.0-1
+ Revision: 643035
- fix group
- import perl-Convert-Bencode

