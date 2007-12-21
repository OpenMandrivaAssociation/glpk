%define	name	glpk
%define	version	4.25
%define	release %mkrel 1

%define lib_name_orig libglpk
%define lib_major 0
%define lib_name                  %mklibname glpk %{lib_major}

%define old_lib_name_devel     	  %mklibname glpk %{lib_major} -d
%define old_lib_name_static_devel %mklibname glpk %{lib_major} -s -d

%define lib_name_devel        	  %mklibname glpk -d
%define lib_name_static_devel 	  %mklibname glpk -s -d

Summary:	GNU Linear Programming Kit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires: 	libgmp
BuildRequires:	gmp-devel, tetex-latex, texinfo

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

%package -n %{lib_name}
Summary:	GLPK shared libraries
Group:		Sciences/Mathematics
Obsoletes:	%{name}
Provides: 	%{lib_name_orig} = %{version}-%{release} 
Provides:	%{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with GLPK and the utilitity glpsol.

%package -n %{lib_name_devel}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides: 	%{lib_name_devel} = %{version}-%{release} 
Obsoletes:	%{old_lib_name_devel}

%description -n %{lib_name_devel}
This package contains the headers needed to develop applications using
GLPK.

%package -n %{lib_name_static_devel}
Summary:	GLPK static libraries
Group: 	 	Development/C
Requires: 	%{lib_name_devel} = %{version}-%{release}
Provides:	%{lib_name_static_devel} = %{version}-%{release}
Obsoletes:	%{old_lib_name_static_devel}

%description -n %{lib_name_static_devel}
This package contains the static libraries necessary for developing
programs which use GLPK. Install this package if you need to statically
link your program or library.

%prep

%setup -q

%build

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.latex
texi2pdf -p gmpl.texi && \
popd

%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# Clean out the examples directory so we can include it wholesale in %doc.
make -C examples distclean
rm -rf examples/Makefile*

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/*.so.*
%attr(0755,root,root) %{_bindir}/glpsol

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc examples doc/*.txt doc/*.pdf AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %{lib_name_static_devel}
%defattr(-, root, root)
%{_libdir}/*.a

