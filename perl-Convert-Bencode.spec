%define upstream_name    Convert-Bencode
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:        %mkrel 1
Summary:        Functions for converting to/from bencoded strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-Bencode/
Source0:        http://www.cpan.org/authors/id/O/OR/ORCLEV/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45


%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make


%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

