%define lib_name_orig libglpk
%define lib_major 0
%define lib_name                  %mklibname %{name} %{lib_major}

%define old_lib_name_devel     	  %mklibname %{name} %{lib_major} -d
%define old_lib_name_static_devel %mklibname %{name} %{lib_major} -s -d

%define lib_name_devel        	  %mklibname %{name} -d
%define lib_name_static_devel 	  %mklibname %{name} -s -d

Summary:	GLPK glpsol utility
Name:		glpk
Version:	4.47
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Requires: 	%{lib_name} = %{version}-%{release}
BuildRequires:	gmp-devel, tetex-latex, texinfo

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the utility glpsol.

%package -n %{lib_name}
Summary:	GLPK shared libraries
Group:		Sciences/Mathematics
Provides: 	%{lib_name_orig} = %{version}-%{release} 

%description -n %{lib_name}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the library needed to run programs dynamically
linked with GLPK.

%package -n %{lib_name_devel}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides: 	%{lib_name_devel} = %{version}-%{release} 
Obsoletes:	%{old_lib_name_devel} < %{version}-%{release} 

%description -n %{lib_name_devel}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the headers needed to develop applications using
GLPK.

%package -n %{lib_name_static_devel}
Summary:	GLPK static libraries
Group: 	 	Development/C
Requires: 	%{lib_name_devel} = %{version}-%{release}
Provides:	%{lib_name_static_devel} = %{version}-%{release}
Obsoletes:	%{old_lib_name_static_devel} < %{version}-%{release} 

%description -n %{lib_name_static_devel}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the static libraries necessary for developing
programs which use GLPK. 

%prep

%setup -q

%build
%configure2_5x
%make

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex
texi2pdf -p gmpl.texi && \
popd

%install
%makeinstall
# Clean out the examples directory so we can include it wholesale in %doc.
%make -C examples distclean
%__rm -rf examples/Makefile*

%files 
%attr(0755,root,root) %{_bindir}/glpsol

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc examples doc/*.txt doc/*.pdf AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.so

%files -n %{lib_name_static_devel}
%{_libdir}/*.a


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.44-2mdv2011.0
+ Revision: 664854
- mass rebuild

* Sun Aug 29 2010 Emmanuel Andry <eandry@mandriva.org> 4.44-1mdv2011.0
+ Revision: 574162
- New version 4.44

* Tue Mar 02 2010 Emmanuel Andry <eandry@mandriva.org> 4.43-1mdv2010.1
+ Revision: 513628
- New version 4.43

* Wed Jan 13 2010 Frederik Himpe <fhimpe@mandriva.org> 4.42-1mdv2010.1
+ Revision: 491049
- update to new version 4.42

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 4.41-1mdv2010.1
+ Revision: 484029
- Update to new version 4.41
- Remove unneeded build hacks (builds with correct CFLAGS now)

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 4.39-1mdv2010.0
+ Revision: 400454
- New version 4.39

* Mon Apr 13 2009 Lev Givon <lev@mandriva.org> 4.37-1mdv2010.0
+ Revision: 366840
- Update to 4.37.
- Update to 4.36.
- Update to 4.35.

* Fri Dec 26 2008 Lev Givon <lev@mandriva.org> 4.34-1mdv2009.1
+ Revision: 319365
- Update to 4.34.

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 4.30-1mdv2009.0
+ Revision: 275804
- New version
- check major

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 4.28-3mdv2009.0
+ Revision: 264554
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Lev Givon <lev@mandriva.org> 4.28-2mdv2009.0
+ Revision: 211204
- Update license.
  Put glpsol binary in a separate package.

* Wed Apr 23 2008 Lev Givon <lev@mandriva.org> 4.28-1mdv2009.0
+ Revision: 196931
- Update to 4.28.
- Update to 4.27.

* Mon Feb 18 2008 Lev Givon <lev@mandriva.org> 4.26-1mdv2008.1
+ Revision: 171766
- Update to 4.26.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Lev Givon <lev@mandriva.org> 4.25-1mdv2008.1
+ Revision: 135932
- Update to 4.25.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Lev Givon <lev@mandriva.org> 4.24-1mdv2008.1
+ Revision: 116578
- Update to 4.24.
  Use new devel library naming policy.
- Update to 4.22, add gmp dependency.

* Sun Aug 05 2007 Lev Givon <lev@mandriva.org> 4.20-1mdv2008.0
+ Revision: 59118
- Update to 4.20.


* Tue Mar 06 2007 Emmanuel Andry <eandry@mandriva.org> 4.15-1mdv2007.0
+ Revision: 133436
- New version 4.15
- fix major
- drop patch (applied upstream)
- Import glpk

* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 4.7-2mdk
- rebuild

* Tue Sep 07 2004 Yoshinori Okuji <yo@nexedi.com> 4.7-1mdk
- New upstream release

