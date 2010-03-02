%define	name	glpk
%define	version	4.43
%define	release %mkrel 1

%define lib_name_orig libglpk
%define lib_major 0
%define lib_name                  %mklibname %{name} %{lib_major}

%define old_lib_name_devel     	  %mklibname %{name} %{lib_major} -d
%define old_lib_name_static_devel %mklibname %{name} %{lib_major} -s -d

%define lib_name_devel        	  %mklibname %{name} -d
%define lib_name_static_devel 	  %mklibname %{name} -s -d

Summary:	GLPK glpsol utility
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires: 	libgmp, %{lib_name} = %{version}-%{release}
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
Obsoletes:	%{name}
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
Obsoletes:	%{old_lib_name_devel}

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
Obsoletes:	%{old_lib_name_static_devel}

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
%__rm -rf %{buildroot}

%makeinstall
# Clean out the examples directory so we can include it wholesale in %doc.
%make -C examples distclean
%__rm -rf examples/Makefile*

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files 
%defattr(-, root, root)
%attr(0755,root,root) %{_bindir}/glpsol

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc examples doc/*.txt doc/*.pdf AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %{lib_name_static_devel}
%defattr(-, root, root)
%{_libdir}/*.a

