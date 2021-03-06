#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-phylobase
Version  : 0.8.10
Release  : 24
URL      : https://cran.r-project.org/src/contrib/phylobase_0.8.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/phylobase_0.8.10.tar.gz
Summary  : Base Package for Phylogenetic Structures and Comparative Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-phylobase-lib = %{version}-%{release}
Requires: R-RNeXML
Requires: R-Rcpp
Requires: R-ade4
Requires: R-ape
Requires: R-rncl
BuildRequires : R-RNeXML
BuildRequires : R-Rcpp
BuildRequires : R-ade4
BuildRequires : R-ape
BuildRequires : R-rncl
BuildRequires : buildreq-R

%description
one or more trees and trait data.

%package lib
Summary: lib components for the R-phylobase package.
Group: Libraries

%description lib
lib components for the R-phylobase package.


%prep
%setup -q -c -n phylobase
cd %{_builddir}/phylobase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589778594

%install
export SOURCE_DATE_EPOCH=1589778594
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylobase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylobase
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylobase
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc phylobase || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/phylobase/DESCRIPTION
/usr/lib64/R/library/phylobase/INDEX
/usr/lib64/R/library/phylobase/Meta/Rd.rds
/usr/lib64/R/library/phylobase/Meta/data.rds
/usr/lib64/R/library/phylobase/Meta/features.rds
/usr/lib64/R/library/phylobase/Meta/hsearch.rds
/usr/lib64/R/library/phylobase/Meta/links.rds
/usr/lib64/R/library/phylobase/Meta/nsInfo.rds
/usr/lib64/R/library/phylobase/Meta/package.rds
/usr/lib64/R/library/phylobase/Meta/vignette.rds
/usr/lib64/R/library/phylobase/NAMESPACE
/usr/lib64/R/library/phylobase/NEWS.md
/usr/lib64/R/library/phylobase/R/phylobase
/usr/lib64/R/library/phylobase/R/phylobase.rdb
/usr/lib64/R/library/phylobase/R/phylobase.rdx
/usr/lib64/R/library/phylobase/data/Rdata.rdb
/usr/lib64/R/library/phylobase/data/Rdata.rds
/usr/lib64/R/library/phylobase/data/Rdata.rdx
/usr/lib64/R/library/phylobase/doc/index.html
/usr/lib64/R/library/phylobase/doc/phylobase.Rnw
/usr/lib64/R/library/phylobase/doc/phylobase.pdf
/usr/lib64/R/library/phylobase/help/AnIndex
/usr/lib64/R/library/phylobase/help/aliases.rds
/usr/lib64/R/library/phylobase/help/paths.rds
/usr/lib64/R/library/phylobase/help/phylobase.rdb
/usr/lib64/R/library/phylobase/help/phylobase.rdx
/usr/lib64/R/library/phylobase/html/00Index.html
/usr/lib64/R/library/phylobase/html/R.css
/usr/lib64/R/library/phylobase/nexmlfiles/comp_analysis.xml
/usr/lib64/R/library/phylobase/nexusfiles/ExContData.Rdata
/usr/lib64/R/library/phylobase/nexusfiles/MultiLineTrees.nex
/usr/lib64/R/library/phylobase/nexusfiles/NastyLabels.nex
/usr/lib64/R/library/phylobase/nexusfiles/NastyLabels2.nex
/usr/lib64/R/library/phylobase/nexusfiles/co1.nex
/usr/lib64/R/library/phylobase/nexusfiles/minNex.nex
/usr/lib64/R/library/phylobase/nexusfiles/minSeq.nex
/usr/lib64/R/library/phylobase/nexusfiles/newick.tre
/usr/lib64/R/library/phylobase/nexusfiles/noStateLabels.nex
/usr/lib64/R/library/phylobase/nexusfiles/shorebird_underscore.nex
/usr/lib64/R/library/phylobase/nexusfiles/testSubsetTaxa.nex
/usr/lib64/R/library/phylobase/nexusfiles/test_min.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeRoundingError.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithContinuousData.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithDiscAndContData.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithDiscreteData.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithPolyExcludedData.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithSpecialCharacters.nex
/usr/lib64/R/library/phylobase/nexusfiles/treeWithUnderscoreLabels.nex
/usr/lib64/R/library/phylobase/tests/misctests.R
/usr/lib64/R/library/phylobase/tests/phylo4dtests.R
/usr/lib64/R/library/phylobase/tests/phylosubtest.R
/usr/lib64/R/library/phylobase/tests/phylotorture.R
/usr/lib64/R/library/phylobase/tests/plottest.R
/usr/lib64/R/library/phylobase/tests/roundtrip.R
/usr/lib64/R/library/phylobase/tests/test-all.R
/usr/lib64/R/library/phylobase/tests/testprune.R
/usr/lib64/R/library/phylobase/tests/testthat/test.checkdata.R
/usr/lib64/R/library/phylobase/tests/testthat/test.class-phylo4.R
/usr/lib64/R/library/phylobase/tests/testthat/test.class-phylo4d.R
/usr/lib64/R/library/phylobase/tests/testthat/test.formatData.R
/usr/lib64/R/library/phylobase/tests/testthat/test.methods-oldclasses.R
/usr/lib64/R/library/phylobase/tests/testthat/test.methods-phylo4.R
/usr/lib64/R/library/phylobase/tests/testthat/test.pdata.R
/usr/lib64/R/library/phylobase/tests/testthat/test.phylo4.R
/usr/lib64/R/library/phylobase/tests/testthat/test.phylobase.options.R
/usr/lib64/R/library/phylobase/tests/testthat/test.prune.R
/usr/lib64/R/library/phylobase/tests/testthat/test.readNCL.R
/usr/lib64/R/library/phylobase/tests/testthat/test.setAs-Methods.R
/usr/lib64/R/library/phylobase/tests/testthat/test.subset.R
/usr/lib64/R/library/phylobase/tests/testthat/test.tbind.R
/usr/lib64/R/library/phylobase/tests/testthat/test.treePlot.R
/usr/lib64/R/library/phylobase/tests/testthat/test.treestruc.R
/usr/lib64/R/library/phylobase/tests/testthat/test.treewalk.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/phylobase/libs/phylobase.so
/usr/lib64/R/library/phylobase/libs/phylobase.so.avx2
/usr/lib64/R/library/phylobase/libs/phylobase.so.avx512
